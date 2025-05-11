<template>
  <el-form :model="form" :rules="rules" ref="loginForm" label-width="100px">
    <el-form-item label="用户名" prop="username">
      <el-input v-model="form.username" placeholder="请输入用户名" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="form.password" type="password" placeholder="请输入密码" autocomplete="off" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitLogin" :loading="loading" :disabled="loading">
        {{ loading ? '登录中...' : '登录' }}
      </el-button>
      <div class="form-link">
        还没有账号？<a href="javascript:;" @click="goToRegister">立即注册</a>
      </div>
    </el-form-item>
  </el-form>
</template>

<script>
// 导入API服务
import { login } from '@/api/user';

export default {
  name: 'LoginForm',
  emits: ['toRegister'],
  data() {
    // 自定义验证函数 - 用户名不能为空
    const validateUsername = (rule, value, callback) => {
      if (!value) {
        callback(new Error('用户名不能为空'));
      } else if (value.trim() === '') {
        callback(new Error('用户名不能只包含空格'));
      } else {
        callback();
      }
    };

    // 自定义验证函数 - 密码不能为空
    const validatePassword = (rule, value, callback) => {
      if (!value) {
        callback(new Error('密码不能为空'));
      } else if (value.trim() === '') {
        callback(new Error('密码不能只包含空格'));
      } else {
        callback();
      }
    };

    return {
      form: {
        username: '',
        password: '',
      },
      rules: {
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' },
          { validator: validateUsername, trigger: 'blur' },
          { min: 3, max: 20, message: '用户名长度在3到20个字符之间', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '密码不能为空', trigger: 'blur' },
          { validator: validatePassword, trigger: 'blur' },
          { min: 6, message: '密码长度不能少于6个字符', trigger: 'blur' }
        ],
      },
      loading: false,
    };
  },
  methods: {
    async submitLogin() {
      // 表单验证
      this.$refs.loginForm.validate(async (valid) => {
        if (!valid) {
          return false;
        }

        // 额外验证用户名和密码不能为空
        if (!this.form.username || this.form.username.trim() === '') {
          this.$message.error('用户名不能为空');
          return false;
        }

        if (!this.form.password || this.form.password.trim() === '') {
          this.$message.error('密码不能为空');
          return false;
        }

        // 设置加载状态
        this.loading = true;

        try {
          // 使用API服务进行登录
          const result = await login(this.form.username, this.form.password);

          if (result.code === 0) {
            // 登录成功，存储token
            localStorage.setItem('token', result.data.token);
            localStorage.setItem('username', this.form.username);

            this.$message.success('登录成功');

            // 这里可以添加登录成功后的路由跳转
            // this.$router.push('/dashboard');
          } else {
            this.$message.error(result.message || '登录失败');
          }
        } catch (error) {
          console.error('登录错误:', error);
          this.$message.error(error.message || '登录失败，请稍后再试');
        } finally {
          // 无论成功失败，都结束loading状态
          this.loading = false;
        }
      });
    },
    // 跳转到注册的方法
    goToRegister() {
      this.$emit('toRegister');
    }
  },
};
</script>

<style scoped>
.el-form {
  max-width: 300px;
  margin: 0 auto;
}

.form-link {
  margin-top: 15px;
  text-align: right;
  font-size: 14px;
}

.form-link a {
  color: #409EFF;
  text-decoration: none;
}

.form-link a:hover {
  text-decoration: underline;
}
</style>