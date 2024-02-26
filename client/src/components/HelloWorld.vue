<template>
  <h1>{{ msg }}</h1>
    <Button @click="count++">count is {{ count }}</Button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Button } from './ui/button'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
