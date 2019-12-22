import { YGOAdapter } from './adapter';
// const createCardElemenets = (cardObj: Response) => {
//   return (
//     `<div id='cards'>
//       <img src={require(../images/pics_small/${cardObj.id}.jpg)} />
//     </div>`
//   );
// };
/* Testing to see if an element is created when we click on a button.
Eventually it'll be a json response
*/
const searchBar: HTMLElement | null = document.getElementById('search');
const cardsDiv: HTMLElement | null = document.getElementById('cards');
//create the mapping to preview cards
// const mapCardJson = (cardsObj: object) => {
//     let cardArray = cardsObj.map(card => )
// }
const createCardElements = (card: string) => {
  return (`
    <div id='cards'>cd
      <h1>${card}</h1>
    </div>
  `);
};

// OnDomLoaded is where we create our code to load.
document.addEventListener('DOMContentLoaded', () => {
  if (searchBar) {
    searchBar.addEventListener('click', (e) => {
      if ((e.target as HTMLInputElement).tagName === 'BUTTON') {
        if (cardsDiv) {
          cardsDiv.innerHTML = createCardElements('something') + cardsDiv.innerHTML;
        }
      }
    });
  }
});
