<template>
  <div class="flex mx-5 mt-96">
    Drag and Drop
    <div 
      class="drop-zone mx-5 pa-12 w-96"
      @drop="onDrop($event, 1)"
      @dragover.prevent
      @dragenter.prevent  
    >
      <div 
        v-for="item in listOne" 
        :key="item.id" 
        class="drag-el"
        :draggable="true"
        @dragstart="startDrag($event, item)"
      >
        {{ item.title }}
      </div>
    </div>
    <div 
      class="drop-zone mx-5 pa-12 w-96"
      @drop="onDrop($event, 2)"
      @dragover.prevent
      @dragenter.prevent  
    >
      <div 
        v-for="item in listTwo" 
        :key="item.id" 
        class="drag-el"
        :draggable="true"
        @dragstart="startDrag($event, item)"
      >
        {{ item.title }}
      </div>
    </div>

    <div 
      v-for="item in listThree" 
      :key="item.id" 
      class="drag-el"
      :draggable="true"
      @dragstart="startDrag($event, item)"
    >
      {{ item.title }}
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref, computed } from 'vue'

type Item = {
  id: number,
  title: string,
  list: number
}

const items = ref([
  {
    id: 0,
    title: 'Item A',
    list: 1,
  },
  {
    id: 1,
    title: 'Item B',
    list: 1,
  },
  {
    id: 2,
    title: 'Item C',
    list: 2,
  },
  {
    id: 3,
    title: 'Stays Put!!',
    list: 3,
  },
])

const startDrag = (event: any, item: Item) => {
  event.dataTransfer.dropEffect = 'move'
  event.dataTransfer.effectAllowed = 'move'
  event.dataTransfer.setData('itemID', item.id)
}

const onDrop = (event: any, list: Item['list']) => {
  const itemID = event.dataTransfer.getData('itemID')
  const itemIndex = items.value.findIndex((item) => item.id == itemID)
  if (itemIndex === -1) throw new Error('Dragging failed: Item not found')

  const item = items.value[itemIndex]
  if (item.list !== 3) {
    item.list = list
  } else {
    const newItem = { ...item, id: Math.floor(Math.random()*100), list }
    items.value.push(newItem)
  }
}

const listOne = computed(() => {
  return items.value.filter((item) => item.list === 1)
})
const listTwo = computed(() => {
  return items.value.filter((item) => item.list === 2)
})
const listThree = computed(() => {
  return items.value.filter((item) => item.list === 3)
})

const fetchTestData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/hello/')

    console.log('Data:', response.data)
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}

fetchTestData()

</script>

<style scoped>
.drop-zone {
  background-color: #eee;
  margin-bottom: 10px;
  padding: 10px;
}

.drag-el {
  background-color: #fff;
  margin-bottom: 10px;
  padding: 5px;
}
</style>
