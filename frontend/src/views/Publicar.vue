<template>
  <Navbar />
  <section class="p-6 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold mb-6 text-[#00A87E]">Crear nueva publicación</h1>

    <form @submit.prevent="generarPublicacion" class="space-y-4">
      <!-- Nombre del negocio (solo lectura) -->
      <div>
        <label class="block font-semibold mb-1">Nombre del negocio</label>
        <input
          v-model="nombreNegocio"
          type="text"
          class="w-full p-2 border rounded bg-gray-100 cursor-not-allowed"
          disabled
        />
      </div>

      <!-- Tipo de negocio (input con autocomplete) -->
      <div class="relative">
        <label class="block font-semibold mb-1">Tipo de negocio *</label>
        <input
          type="text"
          v-model="busqueda"
          @focus="mostrarLista = true"
          @blur="ocultarConRetraso"
          @input="filtrarNegocios"
          placeholder="Escribe o selecciona un negocio"
          class="w-full p-2 border rounded"
          required
        />
        <ul
          v-if="mostrarLista && negociosFiltrados.length"
          class="absolute z-10 w-full bg-white border border-gray-300 rounded shadow-md max-h-60 overflow-y-auto"
        >
          <li
            v-for="negocio in negociosFiltrados"
            :key="negocio.id"
            @mousedown.prevent="seleccionarNegocio(negocio)"
            class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
          >
            {{ negocio.name }}
          </li>
        </ul>
      </div>

      <!-- Tono -->
      <div>
      <label class="block font-semibold mb-1">Tono de la publicación *</label>
      <select v-model="tono" required class="w-full p-2 border rounded">
        <option disabled value="">Selecciona un tono</option>
        <option>Profesional</option>
        <option>Humorístico</option>
        <option>Inspirador</option>
        <option>Informativo</option>
        <option>Emocional</option>
        <option>Creativo</option>
        <option>Casual</option>
        <option>Urgente</option>
        <option>Promocional</option>
        <option>Motivacional</option>
        <option>Reflexivo</option>
        <option>Educativo</option>
        <option>Amigable</option>
        <option>Elegante</option>
        <option>Juvenil</option>
      </select>
    </div>

      <!-- Objetivo -->
      <div>
        <label class="block font-semibold mb-1">Objetivo</label>
        <input
          v-model="objetivo"
          type="text"
          class="w-full p-2 border rounded"
          placeholder="Ej: Aumentar ventas, atraer seguidores..."
        />
      </div>

      <!-- Botón -->
      <div>
        <button
          type="submit"
          class="bg-[#00A87E] text-white px-4 py-2 rounded hover:bg-[#00906D] transition"
          :disabled="loading"
        >
          {{ loading ? 'Creando...' : 'Crear publicación' }}
        </button>
      </div>
    </form>

    <!-- Resultado -->
    <div v-if="resultado" class="mt-6 p-4 bg-gray-100 border rounded whitespace-pre-line">
      <div class="flex justify-between items-center mb-2">
        <h2 class="font-semibold text-lg">Texto generado:</h2>
        <button
          @click="copiarTexto"
          class="bg-[#00A87E] text-white px-3 py-1 rounded text-sm hover:bg-[#00906D] transition flex items-center gap-1"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect width="14" height="14" x="8" y="8" rx="2" ry="2"/>
            <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
          </svg>
          {{ copiado ? 'Copiado!' : 'Copiar texto' }}
        </button>
      </div>
      <p>{{ resultado }}</p>
    </div>

    <!-- Error -->
    <div v-if="error" class="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
      {{ error }}
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from '../components/Navbar.vue'

const nombreNegocio = ref('')
const tipoNegocioId = ref(null)
const busqueda = ref('')
const negocios = ref([])
const negociosFiltrados = ref([])
const mostrarLista = ref(false)
const tono = ref('')
const objetivo = ref('')
const resultado = ref('')
const error = ref('')
const loading = ref(false)
const copiado = ref(false)
const token = localStorage.getItem('token')

const cargarDatosNegocio = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/perfil/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    if (!response.ok) throw new Error('No se pudo cargar los datos del negocio')
    const data = await response.json()

    nombreNegocio.value = data.business_name || ''
    objetivo.value = data.content_goal || ''
    tipoNegocioId.value = data.business_type || null
    
    console.log('Datos del perfil cargados:', data)
    console.log('ID del tipo de negocio:', tipoNegocioId.value)
  } catch (e) {
    error.value = e.message
  }
}

const cargarTiposNegocio = async () => {
  try {
    const res = await fetch('http://localhost:8000/api/business-types/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    if (!res.ok) throw new Error('No se pudo cargar los tipos de negocio')
    const datos = await res.json()
    negocios.value = datos
    negociosFiltrados.value = datos

    console.log('Tipos de negocio cargados:', datos)
    console.log('Buscando ID:', tipoNegocioId.value)

    // Aquí está la corrección principal
    if (tipoNegocioId.value) {
      const tipoActual = datos.find(n => n.id === tipoNegocioId.value)
      if (tipoActual) {
        busqueda.value = tipoActual.name
        console.log('Tipo de negocio encontrado:', tipoActual.name)
      } else {
        console.log('No se encontró el tipo de negocio con ID:', tipoNegocioId.value)
      }
    }
  } catch (e) {
    console.error('Error cargando tipos de negocio:', e)
    error.value = 'Error al cargar los tipos de negocio'
  }
}

const filtrarNegocios = () => {
  const texto = busqueda.value.toLowerCase()
  negociosFiltrados.value = negocios.value.filter(n =>
    n.name?.toLowerCase().includes(texto)
  )
}

const seleccionarNegocio = (negocio) => {
  tipoNegocioId.value = negocio.id
  busqueda.value = negocio.name
  mostrarLista.value = false
}

const ocultarConRetraso = () => {
  setTimeout(() => {
    mostrarLista.value = false
  }, 100)
}

const generarPublicacion = async () => {
  error.value = ''
  resultado.value = ''
  copiado.value = false // Reset estado de copiado
  loading.value = true
  try {
    const response = await fetch('http://localhost:8000/api/crear-publicacion/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({
        business_type: busqueda.value,
        business_name: nombreNegocio.value,
        tone: tono.value,
        objetivo: objetivo.value
      })
    })
    if (!response.ok) {
      const errData = await response.json()
      throw new Error(errData.error || 'Error al generar la publicación')
    }
    const data = await response.json()
    resultado.value = data.content
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

const copiarTexto = async () => {
  try {
    await navigator.clipboard.writeText(resultado.value)
    copiado.value = true
    // Resetear el estado después de 2 segundos
    setTimeout(() => {
      copiado.value = false
    }, 2000)
  } catch (err) {
    console.error('Error al copiar texto:', err)
    // Fallback para navegadores que no soportan clipboard API
    const textArea = document.createElement('textarea')
    textArea.value = resultado.value
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    copiado.value = true
    setTimeout(() => {
      copiado.value = false
    }, 2000)
  }
}

onMounted(async () => {
  await cargarDatosNegocio()
  await cargarTiposNegocio()
})
</script>