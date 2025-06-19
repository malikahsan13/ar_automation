<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" placeholder="Password" type="password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

const router = useRouter()
const email = ref('')
const password = ref('')
const auth = useAuthStore()

const login = async () => {
  await auth.login(email.value, password.value)
  router.push('/dashboard') // create this later
}
</script>
