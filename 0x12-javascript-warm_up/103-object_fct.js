#!/usr/bin/node
function createMyObject() {
  return {
    type: 'object',
    value: 12,
    incr: function () {
      this.value++;
    }
  };
}
const myObject = createMyObject();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
