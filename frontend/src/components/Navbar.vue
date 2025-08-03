<template>
  <nav class="bg-green-600 text-white px-4 py-3 flex items-center justify-between shadow relative">
    <!-- Logo -->
    <div class="flex items-center space-x-2">
      <img src="/logo.png" alt="Logo" class="h-10 w-auto bg-white p-1 rounded-full" />
      <span class="text-2xl font-bold">CreaFacil</span>
    </div>

    <!-- Botón hamburguesa en móviles -->
    <button @click="toggleMobileMenu" class="md:hidden focus:outline-none">
      <MenuIcon class="w-6 h-6 text-white" />
    </button>

    <!-- Menú principal -->
    <div class="hidden md:flex flex-grow justify-between items-center ml-10">
      <!-- Ítems alineados a la izquierda -->
      <ul class="flex space-x-6 text-lg font-medium items-center">
        <li><router-link to="/dashboard" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Inicio</router-link></li>
        <li><router-link to="/crear" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Crear</router-link></li>
       <!-- <li><router-link to="/mis-creaciones" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Mis creaciones</router-link></li>
      --></ul>

      <!-- Icono de usuario a la derecha -->
      <div class="relative" @click="toggleProfileMenu">
        <UserIcon class="w-7 h-7 cursor-pointer hover:text-gray-300 transition" />
        <div
          v-if="isProfileMenuOpen"
          class="absolute right-0 mt-2 w-40 bg-white text-green-600 rounded shadow-md z-50"
        >
          <router-link to="/perfil" class="block px-4 py-2 hover:bg-gray-100">Perfil</router-link>
          <button @click="logout" class="w-full text-left px-4 py-2 hover:bg-gray-100">Cerrar sesión</button>
        </div>
      </div>
    </div>

    <!-- Menú móvil -->
    <div
      v-if="isMobileMenuOpen"
      class="absolute top-full left-0 w-full bg-green-600 text-white flex flex-col px-4 py-3 space-y-2 md:hidden z-50"
    >
      <router-link to="/dashboard" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Inicio</router-link>
      <router-link to="/crear" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Crear</router-link>
      <router-link to="/mis-creaciones" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Mis creaciones</router-link>
      <router-link to="/perfil" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition">Perfil</router-link>
      <button @click="logout" class="hover:bg-white hover:text-green-600 px-3 py-1 rounded transition text-left">Cerrar sesión</button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { MenuIcon, UserIcon } from 'lucide-vue-next'

const router = useRouter()
const isMobileMenuOpen = ref(false)
const isProfileMenuOpen = ref(false)

function toggleMobileMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
  isProfileMenuOpen.value = false
}

function toggleProfileMenu() {
  isProfileMenuOpen.value = !isProfileMenuOpen.value
  isMobileMenuOpen.value = false
}

function logout() {
  localStorage.removeItem('token')
  router.push('/login')
}
</script>
