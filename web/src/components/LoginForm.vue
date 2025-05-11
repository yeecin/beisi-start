<template>
  <el-form :model="form" :rules="rules" ref="loginForm" label-width="100px">
    <el-form-item label="用户名" prop="username">
      <el-input v-model="form.username" placeholder="请输入用户名" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="form.password" type="password" placeholder="请输入密码" autocomplete="off" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitLogin">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
      },
    };
  },
  methods: {
    async submitLogin() {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form),
        });
        const result = await response.json();
        if (result.code === 0) {
          this.$message.success('登录成功');
        } else {
          this.$message.error(result.message);
        }
      } catch (error) {
        this.$message.error('登录失败，请稍后再试');
      }
    },
  },
};
</script>

<style>
.el-form {
  max-width: 300px;
  margin: 0 auto;
}
</style>