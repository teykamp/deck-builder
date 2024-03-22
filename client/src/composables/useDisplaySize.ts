import { ref, watchEffect, onMounted } from 'vue'

export default function useScreenSize() {
    const screenWidth = ref(window.innerWidth)
    const screenHeight = ref(window.innerHeight)
    const xl = ref(false)
    const lg = ref(false)
    const md = ref(false)
    const sm = ref(false)
    const xs = ref(false)
    const smAndDown = ref(false)
    const mdAndDown = ref(false)
    const lgAndDown = ref(false)
    const smAndUp = ref(false)
    const mdAndUp = ref(false)
    const lgAndUp = ref(false)

    const updateScreenSize = () => {
        screenWidth.value = window.innerWidth
        screenHeight.value = window.innerHeight
        if (screenWidth.value < 600) {
            xs.value = true
        } else if (screenWidth.value < 960) {
            sm.value = true
            smAndDown.value = true
        } else if (screenWidth.value < 1264) {
            md.value = true
            mdAndDown.value = true
        } else if (screenWidth.value < 1904) {
            lg.value = true
            lgAndDown.value = true
        } else {
            xl.value = true
        }

        if (screenWidth.value > 1904) {
            lgAndUp.value = true
        } else if (screenWidth.value > 1264) {
            mdAndUp.value = true
        } else if (screenWidth.value > 960) {
            smAndUp.value = true
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
        smAndDown,
        mdAndDown,
        lgAndDown,
        smAndUp,
        mdAndUp,
        lgAndUp, 
        
        
        screenWidth,
        screenHeight
    }
}