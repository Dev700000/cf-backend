<template>
  <div>
    <Navbar /> <!-- Asegúrate que el nombre del componente esté bien registrado -->

    <div class="container mx-auto mt-10 p-4">
      <h1 class="text-2xl font-bold mb-6">Perfil del Usuario</h1>

      <form @submit.prevent="guardarCambios">
        <div class="mb-4">
          <label class="block text-gray-700 font-bold mb-2">Nombre:</label>
          <input
            type="text"
            v-model="perfil.username"
            class="w-full border border-gray-300 rounded px-3 py-2"
            disabled
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-bold mb-2">Nombre del negocio:</label>
          <input
            type="text"
            v-model="perfil.business_name"
            class="w-full border border-gray-300 rounded px-3 py-2"
          />
        </div>

        <div class="mb-4 relative">
          <label class="block text-gray-700 font-bold mb-2">Tipo de negocio:</label>
          <input
            type="text"
            v-model="busqueda"
            placeholder="Escribe para buscar..."
            class="w-full border border-gray-300 rounded px-3 py-2"
            @input="filtrarNegocios"
            autocomplete="off"
          />
          <ul
            v-if="resultados.length"
            class="absolute z-10 bg-white border w-full mt-1 rounded shadow max-h-48 overflow-auto"
          >
            <li
              v-for="tipo in resultados"
              :key="tipo.id"
              @click="seleccionarTipo(tipo)"
              class="px-4 py-2 hover:bg-gray-200 cursor-pointer"
            >
              {{ tipo.nombre }}
            </li>
          </ul>
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-bold mb-2">Descripción del negocio:</label>
          <textarea
            v-model="perfil.business_description"
            class="w-full border border-gray-300 rounded px-3 py-2"
          ></textarea>
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 font-bold mb-2">Objetivo del contenido:</label>
          <textarea
            v-model="perfil.content_goal"
            class="w-full border border-gray-300 rounded px-3 py-2"
          ></textarea>
        </div>

        <button
          type="submit"
          class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
        >
          Guardar Cambios
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '../components/Navbar.vue'

export default {
  components: { Navbar },
  data() {
    return {
      busqueda: '',
      resultados: [],
      perfil: {
        username: '',
        business_name: '',
        business_type: null,
        business_description: '',
        content_goal: ''
      },
      tiposDeNegocio: [
  { id: 1, nombre: "Papelería" },
  { id: 2, nombre: "Ciber café" },
  { id: 3, nombre: "Tienda de abarrotes" },
  { id: 4, nombre: "Estética" },
  { id: 5, nombre: "Consultorio médico" },
  { id: 6, nombre: "Tienda de ropa" },
  { id: 7, nombre: "Cafetería" },
  { id: 8, nombre: "Restaurante" },
  { id: 9, nombre: "Tienda de electrónica" },
  { id: 10, nombre: "Puesto de comida" },
  { id: 11, nombre: "Peluquería" },
  { id: 12, nombre: "Tienda naturista" },
  { id: 13, nombre: "Panadería" },
  { id: 14, nombre: "Tortillería" },
  { id: 15, nombre: "Refaccionaria" },
  { id: 16, nombre: "Taller mecánico" },
  { id: 17, nombre: "Ferretería" },
  { id: 18, nombre: "Miscelánea" },
  { id: 19, nombre: "Venta de accesorios para celulares" },
  { id: 20, nombre: "Renta de computadoras" },
  { id: 21, nombre: "Renta de videojuegos" },
  { id: 22, nombre: "Imprenta" },
  { id: 23, nombre: "Agencia de viajes" },
  { id: 24, nombre: "Despacho contable" },
  { id: 25, nombre: "Estudio fotográfico" },
  { id: 26, nombre: "Centro de copiado" },
  { id: 27, nombre: "Escuela de idiomas" },
  { id: 28, nombre: "Consultorio dental" },
  { id: 29, nombre: "Clínica veterinaria" },
  { id: 30, nombre: "Gimnasio" },
  { id: 31, nombre: "Spa" },
  { id: 32, nombre: "Lavandería" },
  { id: 33, nombre: "Tintorería" },
  { id: 34, nombre: "Tienda de regalos" },
  { id: 35, nombre: "Florería" },
  { id: 36, nombre: "Boutique" },
  { id: 37, nombre: "Zapatería" },
  { id: 38, nombre: "Tienda de disfraces" },
  { id: 39, nombre: "Juguetería" },
  { id: 40, nombre: "Distribuidora de productos de limpieza" },
  { id: 41, nombre: "Venta de cosméticos" },
  { id: 42, nombre: "Tienda de artículos religiosos" },
  { id: 43, nombre: "Papelería mayorista" },
  { id: 44, nombre: "Tienda de computadoras" },
  { id: 45, nombre: "Centro de servicio técnico" },
  { id: 46, nombre: "Venta de autopartes" },
  { id: 47, nombre: "Venta de herramientas" },
  { id: 48, nombre: "Cerrajería" },
  { id: 49, nombre: "Tienda de mascotas" },
  { id: 50, nombre: "Venta de artículos deportivos" },
  { id: 51, nombre: "Tienda de ciclismo" },
  { id: 52, nombre: "Venta de uniformes" },
  { id: 53, nombre: "Estudio de tatuajes" },
  { id: 54, nombre: "Estudio de uñas" },
  { id: 55, nombre: "Barbería" },
  { id: 56, nombre: "Tienda de vinos y licores" },
  { id: 57, nombre: "Mini super" },
  { id: 58, nombre: "Distribuidora de alimentos" },
  { id: 59, nombre: "Frutería" },
  { id: 60, nombre: "Carnicería" },
  { id: 61, nombre: "Pescadería" },
  { id: 62, nombre: "Verdulería" },
  { id: 63, nombre: "Heladería" },
  { id: 64, nombre: "Rosticería" },
  { id: 65, nombre: "Tienda orgánica" },
  { id: 66, nombre: "Tienda de té y café" },
  { id: 67, nombre: "Rosticería de pollos" },
  { id: 68, nombre: "Venta de artículos para fiesta" },
  { id: 69, nombre: "Tienda de refacciones para motos" },
  { id: 70, nombre: "Almacén de herramientas" },
  { id: 71, nombre: "Distribuidora de papel" },
  { id: 72, nombre: "Tienda de cómics" },
  { id: 73, nombre: "Tienda de videojuegos" },
  { id: 74, nombre: "Centro cultural" },
  { id: 75, nombre: "Editorial independiente" },
  { id: 76, nombre: "Tienda de productos ecológicos" },
  { id: 77, nombre: "Tienda de decoración" },
  { id: 78, nombre: "Tienda de artículos para el hogar" },
  { id: 79, nombre: "Distribuidora de plásticos" },
  { id: 80, nombre: "Venta de artesanías" },
  { id: 81, nombre: "Tienda de segunda mano" },
  { id: 82, nombre: "Tienda de reciclaje" },
  { id: 83, nombre: "Casa de empeño" },
  { id: 84, nombre: "Tienda de productos coreanos" },
  { id: 85, nombre: "Venta de celulares" },
  { id: 86, nombre: "Tienda de fundas y accesorios" },
  { id: 87, nombre: "Centro de desarrollo infantil" },
  { id: 88, nombre: "Escuela de música" },
  { id: 89, nombre: "Clases particulares" },
  { id: 90, nombre: "Academia de baile" },
  { id: 91, nombre: "Tienda de instrumentos musicales" },
  { id: 92, nombre: "Academia de computación" },
  { id: 93, nombre: "Clases de regularización" },
  { id: 94, nombre: "Guardería" },
  { id: 95, nombre: "Tienda de repostería" },
  { id: 96, nombre: "Tienda de productos sin gluten" },
  { id: 97, nombre: "Comida vegana" },
  { id: 98, nombre: "Dark kitchen" },
  { id: 99, nombre: "Tienda de artículos escolares" },
  { id: 100, nombre: "Tienda de productos importados" },
]
,
      token: localStorage.getItem('token')
    }
  },
  methods: {
    filtrarNegocios() {
      const texto = this.busqueda.toLowerCase()
      this.resultados = this.tiposDeNegocio.filter(tipo =>
        tipo.nombre.toLowerCase().includes(texto)
      )
    },
    seleccionarTipo(tipo) {
      this.perfil.business_type = tipo.id  // Guardas solo el id
      this.busqueda = tipo.nombre           // Mostrar el nombre en el input
      this.resultados = []                   // Limpiar resultados
    },
    async obtenerPerfil() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/perfil/', {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        })
        this.perfil = {
          username: response.data.username,
          business_name: response.data.business_name || '',
          business_type: response.data.business_type || null,
          business_description: response.data.business_description || '',
          content_goal: response.data.content_goal || ''
        }

        // Mostrar el nombre correspondiente en la búsqueda
        const tipo = this.tiposDeNegocio.find(t => t.id === this.perfil.business_type)
        this.busqueda = tipo ? tipo.nombre : ''
      } catch (error) {
        console.error('Error al obtener perfil:', error)
      }
    },
    async guardarCambios() {
      try {
        await axios.patch('http://127.0.0.1:8000/api/perfil/', {
          business_name: this.perfil.business_name,
          business_type: this.perfil.business_type,
          business_description: this.perfil.business_description,
          content_goal: this.perfil.content_goal
        }, {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        })
        alert('Cambios guardados correctamente.')
      } catch (error) {
        console.error('Error al guardar perfil:', error)
        alert('Error al guardar los cambios.')
      }
    }
  },
  mounted() {
    this.obtenerPerfil()
  }
}
</script>

<style scoped>
.container {
  max-width: 700px;
}
</style>
