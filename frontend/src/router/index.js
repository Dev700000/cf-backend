import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Perfil from '../views/Perfil.vue'
import Login from '../views/login.vue'
import Publicar from '../views/Publicar.vue'
import MisPublicaciones from '../views/MisPublicaciones.vue'
import Register from '../views/Register.vue'
import Landing from '../views/Landing.vue'
import ConfNegocio from '../views/ConfNegocio.vue'

const routes = [
  { path: '/', component: Landing },
  { path: '/login', component: Login },
  { path: '/registrar', component: Register },
  {
    path: '/dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/crear',
    component: Publicar,
    meta: { requiresAuth: false }
  },
  {
    path: '/conf-negocio',
    component: ConfNegocio,
    meta: { requiresAuth: true }
  },
  {
    path: '/perfil',
    component: Perfil,
    meta: { requiresAuth: true }
  },
  {
    path: '/mis-creaciones',
    component: MisPublicaciones,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  // Si la ruta requiere estar autenticado y no hay token
  if (to.meta.requiresAuth && !token) {
    return next('/login')
  }

  // Si la ruta es solo para invitados y hay token
  if (to.meta.requiresGuest && token) {
    return next('/dashboard')
  }

  next()
})
export default router
