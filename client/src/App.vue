<template>
  <div class="flex" v-if="lg || xl">
  </div>
</template>

<script setup lang="ts">
import useScreenSize from '@/composables/useDisplaySize'

const { lg, xl } = useScreenSize()
</script>