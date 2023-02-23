import {Component} from "./component.js";

class PostCard extends Component {
  createdAt = undefined;
  name = undefined;
  email = undefined;
  content = undefined;

  constructor(props) {
    super();
    this.createdAt = props.createdAt;
    this.name = props.name;
    this.email = props.email;
    this.content = props.content;
  }

  build() {
    const card = document.createElement("div");
    const cardBody = document.createElement("div");
    const cardTitle = document.createElement("h4");
    const cardSubtitle = document.createElement("h6");
    const cardText = document.createElement("p");

    card.classList.add("card", "mb-3");
    cardBody.classList.add("card-body");
    cardTitle.classList.add("card-title");
    cardSubtitle.classList.add("card-subtitle");
    cardText.classList.add("card-text");

    cardTitle.innerText = this.name;
    cardSubtitle.innerText = this.email;
    cardText.innerText = this.content;

    card.appendChild(cardBody);
    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardSubtitle);
    cardBody.appendChild(cardText);

    return card;
  }
}

export {PostCard};
