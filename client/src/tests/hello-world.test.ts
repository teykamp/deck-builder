import { test, expect, vi } from "vitest"
import { mount } from "@vue/test-utils"

import HelloWorld from "@/components/HelloWorld.vue"

vi.mock('axios', () => ({
    default: {
        get: () => Promise.resolve({ data: {} })
    }
}))

test("mount component", async () => {
    expect(HelloWorld).toBeTruthy()

    const wrapper = mount(HelloWorld)
    expect(wrapper.text()).toContain("Drag and Drop")
})