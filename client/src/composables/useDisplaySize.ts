import { ref, watchEffect, onMounted } from 'vue'

export default function useScreenSize() {
    const screenWidth = ref(window.innerWidth)
    const screenHeight = ref(window.innerHeight)
    const xl = ref(false)
    const lg = ref(false)
    const md = ref(false)
    const sm = ref(false)
    const xs = ref(false)

    const updateScreenSize = () => {
        screenWidth.value = window.innerWidth
        screenHeight.value = window.innerHeight
        if (screenWidth.value < 600) {
            xs.value = true
        } else if (screenWidth.value < 960) {
            sm.value = true
        } else if (screenWidth.value < 1264) {
            md.value = true
        } else if (screenWidth.value < 1904) {
            lg.value = true
        } else {
            xl.value = true
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
        xs,
        sm,
        md,
        lg,
        xl,
        screenWidth,
        screenHeight
    }
}