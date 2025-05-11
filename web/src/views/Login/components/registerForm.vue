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
      <el-button type="primary" @click="submitRegister" :loading="loading" :disabled="loading">
        {{ loading ? '注册中...' : '注册' }}
      </el-button>
      <div class="form-link">
        已有账号？<a href="javascript:;" @click="goToLogin">立即登录</a>
      </div>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  name: 'RegisterForm',
  emits: ['toLogin'],
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
        confirmPassword: '',
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
        confirmPassword: [
          { required: true, message: '请确认密码', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (!value) {
                callback(new Error('确认密码不能为空'));
              } else if (value !== this.form.password) {
                callback(new Error('两次输入的密码不一致'));
              } else {
                callback();
              }
            },
            trigger: 'blur',
          },
        ],
      },
      loading: false,
    };
  },
  methods: {
    async submitRegister() {
      // 表单验证
      this.$refs.registerForm.validate(async (valid) => {
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
          const response = await fetch('http://120.76.99.179:5000/api/register', {
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
            // 注册成功后切换到登录页
            setTimeout(() => {
              this.goToLogin();
            }, 1500);
          } else {
            this.$message.error(result.message || '注册失败');
          }
        } catch (error) {
          console.error('注册错误:', error);
          this.$message.error('注册失败，请稍后再试');
        } finally {
          // 无论成功失败，都结束loading状态
          this.loading = false;
        }
      });
    },
    // 跳转到登录的方法
    goToLogin() {
      this.$emit('toLogin');
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