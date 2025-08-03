<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-100 to-green-200">
    <div class="bg-white shadow-2xl rounded-2xl px-10 py-12 w-full max-w-2xl border-t-4 border-green-500">
      <h1 class="text-3xl font-extrabold text-center text-green-700 mb-6">Configura tu Negocio</h1>
      <p class="text-center text-gray-500 mb-6">Completa la información de tu empresa para comenzar a usar el sistema</p>

      <form @submit.prevent="handleSubmit">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Nombre del negocio</label>
            <input
              v-model="business.name"
              type="text"
              required
              placeholder="Ej. Ciber El Rayo"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Tipo de negocio</label>
            <input
              v-model="business.type"
              type="text"
              required
              placeholder="Ej. Papelería, café internet"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
            />
          </div>

          <div class="md:col-span-2">
            <label class="block text-sm font-semibold text-gray-700 mb-1">Descripción</label>
            <textarea
              v-model="business.description"
              rows="3"
              placeholder="Describe brevemente tu negocio"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
            ></textarea>
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Sitio web o redes sociales</label>
            <input
              v-model="business.website"
              type="url"
              placeholder="https://tubusiness.com"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Logo (opcional)</label>
            <input
              type="file"
              accept="image/*"
              @change="handleFileUpload"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg"
            />
          </div>
        </div>

        <button
          type="submit"
          class="mt-8 w-full bg-green-600 text-white font-semibold py-2 rounded-lg hover:bg-green-700 transition-all"
        >
          Guardar y continuar
        </button>

        <p v-if="error" class="mt-4 text-center text-red-600 font-medium">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const error = ref('')
const business = ref({
  name: '',
  type: '',
  description: '',
  website: '',
  logo: null,
})

const handleFileUpload = (e) => {
  business.value.logo = e.target.files[0]
}

const handleSubmit = async () => {
  try {
    const formData = new FormData()
    formData.append('name', business.value.name)
    formData.append('type', business.value.type)
    formData.append('description', business.value.description)
    formData.append('website', business.value.website)
    if (business.value.logo) {
      formData.append('logo', business.value.logo)
    }

    const token = localStorage.getItem('token')
    const response = await fetch('http://localhost:8000/api/negocio/', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    })

    if (!response.ok) {
      throw new Error('No se pudo guardar la información del negocio')
    }

    router.push('/dashboard')
  } catch (err) {
    error.value = err.message || 'Error al guardar los datos'
  }
}
</script>
