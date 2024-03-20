import { ref, watchEffect, onMounted } from 'vue'

export default function useScreenSize() {
    const screenWidth = ref(window.innerWidth)
    const screenHeight = ref(window.innerHeight)
    const breakPoint = ref<'xs' | 'sm' | 'md' | 'lg' | 'xl' | null>(null)

    const updateScreenSize = () => {
        screenWidth.value = window.innerWidth
        screenHeight.value = window.innerHeight
        if (screenWidth.value < 600) {
            breakPoint.value = 'xs'
        } else if (screenWidth.value < 960) {
            breakPoint.value = 'sm'
        } else if (screenWidth.value < 1264) {
            breakPoint.value = 'md'
        } else if (screenWidth.value < 1904) {
            breakPoint.value = 'lg'
        } else {
            breakPoint.value = 'xl'
        }
    }

    watchEffect(() => {
        window.addEventListener('resize', updateScreenSize)

        return () => {
            window.removeEventListener('resize', updateScreenSize)
        }
    })

    onMounted(() => updateScreenSize())

    return {
        breakPoint,
        screenWidth,
        screenHeight
    }
}