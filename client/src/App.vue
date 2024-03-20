<template>
  {{ breakPoint }}
</template>

<script setup lang="ts">
import useScreenSize from '@/composables/useDisplaySize'

const { breakPoint } = useScreenSize()
</script>