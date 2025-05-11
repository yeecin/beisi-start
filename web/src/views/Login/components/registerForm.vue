<template>
  <el-form :model="form" :rules="rules" ref="registerForm" label-width="100px">
    <el-form-item label="用户名" prop="username">
      <el-input v-model="form.username" placeholder="请输入用户名" autocomplete="off" />
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="form.password" type="password" placeholder="请输入密码" autocomplete="off" />
    </el-form-item>
    <el-form-item label="确认密码" prop="confirmPassword">
      <el-input
          v-model="form.confirmPassword"
          type="password"
          placeholder="请再次输入密码"
          autocomplete="off"
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitRegister">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'RegisterForm',
  data() {
    return {
      form: {
        username: '',
        password: '',
        confirmPassword: '',
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        confirmPassword: [
          { required: true, message: '请确认密码', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value !== this.form.password) {
                callback(new Error('两次输入的密码不一致'));
              } else {
                callback();
              }
            },
            trigger: 'blur',
          },
        ],
      },
    };
  },
  methods: {
    async submitRegister() {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.form.username,
            password: this.form.password,
          }),
        });
        const result = await response.json();
        if (result.code === 0) {
          this.$message.success('注册成功');
        } else {
          this.$message.error(result.message);
        }
      } catch (error) {
        this.$message.error('注册失败，请稍后再试');
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