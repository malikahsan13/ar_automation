<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" placeholder="Password" type="password" />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

const register = async () => {
  await axios.post('http://localhost:8000/auth/register', {
    email: email.value,
    password: password.value
  })
  router.push('/login')
}
</script>
