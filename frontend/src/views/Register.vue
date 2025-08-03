<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-100 to-green-200">
    <div class="bg-white shadow-2xl rounded-2xl px-10 py-12 w-full max-w-md border-t-4 border-green-500">
      <h1 class="text-3xl font-extrabold text-center text-green-700 mb-6">Crear Cuenta</h1>
      <p class="text-center text-gray-500 mb-6">Regístrate para empezar a usar la aplicación</p>

      <form @submit.prevent="handleRegister">
        <div class="mb-5">
          <label class="block text-sm font-semibold text-gray-700 mb-1">Nombre de usuario (Sin espacios)</label>
          <input
            v-model="username"
            type="text"
            required
            placeholder="tu usuario"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
          />
        </div>

        <div class="mb-5">
          <label class="block text-sm font-semibold text-gray-700 mb-1">Correo electrónico</label>
          <input
            v-model="email"
            type="email"
            required
            placeholder="tucorreo@ejemplo.com"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
          />
        </div>

        <div class="mb-5">
          <label class="block text-sm font-semibold text-gray-700 mb-1">Contraseña</label>
          <input
            v-model="password"
            type="password"
            required
            placeholder="********"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
          />
        </div>

        <div class="mb-6">
          <label class="block text-sm font-semibold text-gray-700 mb-1">Confirmar contraseña</label>
          <input
            v-model="password2"
            type="password"
            required
            placeholder="********"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-green-600 text-white font-semibold py-2 rounded-lg hover:bg-green-700 transition-all"
          :disabled="loading"
        >
          {{ loading ? "Registrando..." : "Crear Cuenta" }}
        </button>
      </form>

      <p v-if="error" class="mt-4 text-center text-red-600 font-medium">{{ error }}</p>
      <p v-if="success" class="mt-4 text-center text-green-700 font-medium">{{ success }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('')
const error = ref('')
const success = ref('')
const loading = ref(false)
const router = useRouter()

const handleRegister = async () => {
  error.value = ''
  success.value = ''
  loading.value = true

  try {
    const response = await fetch('http://localhost:8000/api/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
        password2: password2.value
      })
    })

    const data = await response.json()

    if (!response.ok) {
      error.value = Object.values(data).flat().join(' ') || 'Error al registrar'
      loading.value = false
      return
    }

    success.value = 'Usuario creado con éxito, redirigiendo al login...'
    loading.value = false

    setTimeout(() => {
      router.push('/login')
    }, 2000)

  } catch (e) {
    error.value = 'Error de conexión o servidor'
    loading.value = false
  }
}
</script>
