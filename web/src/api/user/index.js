/**
 * 用户相关API服务
 */

const API_BASE_URL = 'http://YourBaseUrl/api';

/**
 * 用户登录
 * @param {string} username - 用户名
 * @param {string} password - 密码
 * @returns {Promise} - 返回登录结果的Promise
 */
export const login = async (username, password) => {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        return await response.json();
    } catch (error) {
        console.error('登录请求失败:', error);
        throw new Error('网络错误，请检查您的网络连接');
    }
};

/**
 * 用户注册
 * @param {string} username - 用户名
 * @param {string} password - 密码
 * @returns {Promise} - 返回注册结果的Promise
 */
export const register = async (username, password) => {
    try {
        const response = await fetch(`${API_BASE_URL}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        return await response.json();
    } catch (error) {
        console.error('注册请求失败:', error);
        throw new Error('网络错误，请检查您的网络连接');
    }
};

/**
 * 获取用户信息
 * @returns {Promise} - 返回用户信息的Promise
 */
export const getUserInfo = async () => {
    try {
        const token = localStorage.getItem('token');
        if (!token) {
            throw new Error('未登录');
        }

        const response = await fetch(`${API_BASE_URL}/user/info`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        });

        return await response.json();
    } catch (error) {
        console.error('获取用户信息失败:', error);
        throw error;
    }
};

/**
 * 退出登录
 */
export const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
};
