<template>
  <h1>{{ msg }}</h1>
    <Button @click="count++">count is {{ count }}</Button>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'

defineProps<{ msg: string }>()

const count = ref(0)
</script>
