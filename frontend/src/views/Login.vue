<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-100 to-green-200">
    <div class="bg-white shadow-2xl rounded-2xl px-10 py-12 w-full max-w-md border-t-4 border-green-500">
      <h1 class="text-3xl font-extrabold text-center text-green-700 mb-6">Bienvenido</h1>
      <p class="text-center text-gray-500 mb-6">Por favor, inicia sesión para continuar</p>

      <form @submit.prevent="handleLogin">
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

        <div class="mb-6">
          <label class="block text-sm font-semibold text-gray-700 mb-1">Contraseña</label>
          <input
            v-model="password"
            type="password"
            required
            placeholder="********"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:outline-none"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-green-600 text-white font-semibold py-2 rounded-lg hover:bg-green-700 transition-all"
        >
          Iniciar Sesión
        </button>
      </form>
      <a href="/registrar" class="text-center text-sm text-green-600 hover:underline">¿No tienes una cuenta? Regístrate</a>
      <p v-if="error" class="mt-4 text-center text-red-600 font-medium">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const handleLogin = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    })

    if (!response.ok) {
      throw new Error('Credenciales incorrectas')
    }

    const data = await response.json()

    // Guardamos el token que envía el backend
    localStorage.setItem('token', data.access)  // 'access' si usas SimpleJWT

    router.push('/crear')
  } catch (err) {
    error.value = err.message || 'Error al iniciar sesión'
  }
}
</script>

