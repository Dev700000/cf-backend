<template>
  <div class="min-h-screen bg-gradient-to-br from-green-100 to-green-200 flex flex-col">
    <!-- Navbar -->
    <nav class="bg-white shadow-md">
      <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-green-700">CreaFacil</h1>
        <div>
          <a href="#features" class="text-green-700 hover:underline mr-6 font-semibold">Características</a>
          <a href="#benefits" class="text-green-700 hover:underline mr-6 font-semibold">Beneficios</a>
          <a href="/login" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition">Iniciar Sesión</a>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="flex-grow flex flex-col items-center justify-center text-center px-6 py-20 max-w-4xl mx-auto">
      <h2 class="text-4xl md:text-5xl font-extrabold text-green-800 mb-6">
        Potencia tu negocio con contenido que conecta
      </h2>
      <p class="text-green-700 text-lg mb-10">
        Nuestro sistema SaaS te ayuda a crear publicaciones, promociones y contenido efectivo para tus redes sociales, adaptado a tu negocio y audiencia.
      </p>
      <a href="/registrar" class="bg-green-600 text-white font-semibold px-8 py-3 rounded-lg hover:bg-green-700 transition">
        Comienza Gratis
      </a>
    </section>

    <!-- Features Section -->
    <section id="features" class="bg-white py-20 px-6 max-w-6xl mx-auto rounded-xl shadow-lg mb-20">
      <h3 class="text-3xl font-bold text-green-700 mb-12 text-center">Características principales</h3>
      <div class="grid md:grid-cols-3 gap-12 text-green-800">
        <div class="flex flex-col items-center text-center">
          <svg class="w-16 h-16 mb-4 text-green-500" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 20h9"/></svg>
          <h4 class="text-xl font-semibold mb-2">Publicaciones Personalizadas</h4>
          <p>Crea contenido adaptado a tu tipo de negocio, tono y objetivos.</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <svg class="w-16 h-16 mb-4 text-green-500" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>
          <h4 class="text-xl font-semibold mb-2">Galería de Imágenes</h4>
          <p>Accede a imágenes prediseñadas para enriquecer tus posts fácilmente.</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <svg class="w-16 h-16 mb-4 text-green-500" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M5 12h14"/></svg>
          <h4 class="text-xl font-semibold mb-2">Historial y Gestión</h4>
          <p>Mantén un registro ordenado de todas tus publicaciones creadas.</p>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section id="benefits" class="max-w-6xl mx-auto px-6 mb-20 text-green-900">
      <h3 class="text-3xl font-bold mb-10 text-center">¿Por qué elegirnos?</h3>
      <ul class="list-disc list-inside space-y-4 max-w-3xl mx-auto text-lg">
        <li>Ahorra tiempo automatizando la creación de contenido.</li>
        <li>Mejora la conexión con tu audiencia con mensajes personalizados.</li>
        <li>Fácil de usar, sin conocimientos técnicos previos.</li>
        <li>Soporte continuo para ayudarte a crecer tu negocio.</li>
      </ul>
    </section>

    <!-- Call to Action -->
    <section class="bg-green-600 py-12 text-center text-white">
      <h4 class="text-2xl font-semibold mb-4">¿Listo para transformar tu presencia en línea?</h4>
      <a href="/registrar" class="bg-white text-green-700 px-8 py-3 rounded-lg font-bold hover:bg-green-100 transition">
        Regístrate Ahora
      </a>
    </section>

    <!-- Footer -->
    <footer class="bg-green-700 text-green-200 py-6 mt-auto">
      <div class="max-w-7xl mx-auto text-center text-sm">
        &copy; 2025 ContentSaaS. Todos los derechos reservados.
      </div>
    </footer>
  </div>
</template>

<script setup>
// No scripts necesarios para la landing estática
</script>

<style scoped>
/* Puedes agregar estilos personalizados si quieres */
</style>
