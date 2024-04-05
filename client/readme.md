# Client Details

## Getting started
- [Vue](https://vuejs.org/) - Framework
- [shad cn](https://www.shadcn-vue.com/) - UI Library
- [Vitest](https://vitest.dev/guide/) - Testing Library
- [Tailwind](https://tailwindcss.com/) - Styling
- [Pinia](https://pinia.vuejs.org/) - Global State Management

## Style Guide
Format Vue directives on top, then events, then v-bind attributes, then additional props.
```ts
<div
	v-for="item in listTwo"
	:key="item.id"
	@dragstart="startDrag($event, item)"
	:draggable="true"
	class="drag-el"
></div>
```
Don't use semicolons unless required (i.e. a for loop).
Avoid nested if statements. Prefer returning out of function when possible.
Create types where possible. Prefer unions and using existing types. Do not declare types where they can be inferred unless initializing a variable to `null`. Initialize variables to `null` instead of `undefined`.
Prefer longer names to avoid comments. Make code self-evident wherever possible.
2 spaces for indentation rather than tabs

## Commands
`npm run dev` - start development server
`npm run test` - run tests
`npm run build` build to dist

## Testing
We test both components and functions. Please write adequate tests for component actions and state and for checking functions where necessary. The development style is to write tests afterwards instead of test-driven-development, however you are free to write code how you please.
