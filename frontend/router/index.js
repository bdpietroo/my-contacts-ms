/**
 * Configuração do Vue Router para a aplicação.
 * 
 * Define as rotas do frontend, mapeando cada URL para o seu repespectivo componente Vue.
 */

import { createRouter, createWebHistory } from 'vue-router';
import Login from '../src/views/Login.vue';
import Contacts from '../src/views/Contacts.vue';

const routes = [
  // Rota para a página de login
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  // Rota para a página de contatos 
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts,

    beforeEnter: function (to, from, next) {
      // Verifica se o parâmetro de query 'login_success' está presente
      if (to.query.login_success) {
        next(); // Permite o acesso
      } else {
        next('/'); // Redireciona para o login
      }
    }
  }
];

// Cria a instância do router
const router = createRouter({
  // Habilita o "history mode" para URLs limpas
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;