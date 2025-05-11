import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login/Login.vue';

const routes = [
    { path: '/', redirect: '/login' }, // 根路径重定向到登录页面
    { path: '/login', component: Login, meta: { title: '登录' } },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;