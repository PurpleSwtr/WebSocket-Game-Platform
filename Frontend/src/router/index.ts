import { createRouter, createWebHistory } from 'vue-router'
import Main from "@/views/Main.vue"
import Session from '@/views/Session.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
    path: '/',
    children: [
      {
        path: '',
        component: Main,
      },
      {
        path: 'session/:id',
        component: Session,
      }
    ]
  }],
})

export default router
