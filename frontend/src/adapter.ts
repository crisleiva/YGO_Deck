class YGOAdapter {

  public getAllCards = () => {
    const ygoUrl = 'www.localhost:5000/api/v1/cards/all';
    return fetch(ygoUrl)
      .then((res) => {
        if (!res.ok) {
          throw new Error(res.statusText);
        }
        return res.json();
      });
  }

  public getCard = (option: string, param: string) => {
    const ygoUrl = `www.localhost:5000/api/v1/card/${option}/${param}`;
    return fetch(ygoUrl)
      .then((res) => {
        if (!res.ok) {
          throw new Error(res.statusText);
        }
        return res.json();
      });
  }

}

export default YGOAdapter;
