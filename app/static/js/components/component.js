class Component {
  constructor() {}

  build(...args) {
    throw new Error(`Method not implemented; passed args: ${args}`);
  }
}

export {Component};
