import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5000/api', // 后端接口地址
    withCredentials: true, // 允许发送 Cookies
    headers: {
        'Content-Type': 'application/json',
    },
});

// 请求拦截器，附加 Token
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api;
