<template>
  <h1>{{ msg }}</h1>
    <Button @click="count++">count is {{ count }}</Button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'

import axios from 'axios'

defineProps<{ msg: string }>()

const count = ref(0)

const fetchTestData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/hello/')

    console.log('Data:', response.data)
  } catch (error) {
    console.error('Error fetching data:', error.message)
  }
}

fetchTestData()
</script>
