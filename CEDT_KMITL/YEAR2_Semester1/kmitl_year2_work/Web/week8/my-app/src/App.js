import React from "react";
import "./App.css";

// component
const Food = ({ name, count, onVote, onUnVote }) => {
  let displayCount;
  if (count === 0) {
    displayCount = "Min";
  } else if (count === 10) {
    displayCount = "Max";
  } else {
    displayCount = count;
  }

  return (
    <div className="Food">
      <h2>{name}</h2>
      <button onClick={onVote}>Click to Vote</button>
      <button onClick={onUnVote}>Click to Vote</button>
      <div className="txtCount">{displayCount}</div>
    </div>
  );
};

class App extends React.Component {
  state = {
    foods: [
      { name: "ข้าวผัด", count: 0 },
      { name: "ผัดไทย", count: 0 },
    ],
  };

  onVote = (name) => {
    const foods = this.state.foods.map((food) => {
      if (food.name === name) {
        food.count++;
        if (food.count >= 11) {
          alert("จำนวนโหวตสูงสุดคือ 10");
          food.count = 10;
        } else if (food.count < 0) {
          alert("โหวตไม่ได้");
          food.count = 0;
        }
      }
      return food;
    });

    this.setState({ foods });
  };

  onUnVote = (name) => {
    const foods = this.state.foods.map((food) => {
      if (food.name === name) {
        food.count--;
        if (food.count < 0) {
          alert("โหวตไม่ได้");
          food.count = 0;
        }
      }
      return food;
    });

    this.setState({ foods });
  };

  render() {
    return (

      <div className="App">
        <style>
          
        </style>
        <header className="App-header">
          <h1 className="App-title">โหวตอาหาร</h1>
        </header>
        <div className="container-main">
          <div className="container-text-and-img">
            <div className="box-content">
              <div className="food-catagories">อาหารคาว</div>
              <div className="food-name">ข้าวผัด</div>
              <div className="food-description">
                <br></br>
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s, when an unknown printer took a galley
                of type and scrambled it to make a type specimen book. It has
                survived not only five centuries, but also the leap into
                electronic typesetting, remaining essentially unchanged. It was
                popularised in the 1960s with the release of Letraset sheets
              </div>
            </div>
            <img
              src="https://www.ajinomoto.co.th//storage/photos/shares/our-story/tips/friedrice/62ff47ff5a301.jpg"
              width="250px"
              alt="ข้าวผัด"
            />
          </div>
          {this.state.foods.map((food) => {
            if (food.name === "ข้าวผัด") {
              return (
                <Food
                  key={food.name}
                  count={food.count}
                  onVote={() => this.onVote(food.name)}
                  onUnVote={() => this.onUnVote(food.name)}
                />
              );
            }else {
              return null;
            }
          })}
        </div>
        <div className="container-main">
          <div className="container-text-and-img">
            <div className="box-content">
              <div className="food-catagories">อาหารคาว</div>
              <div className="food-name">ผัดไทย</div>
              <div className="food-description">
                <br></br>
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s, when an unknown printer took a galley
                of type and scrambled it to make a type specimen book. It has
                survived not only five centuries, but also the leap into
                electronic typesetting, remaining essentially unchanged. It was
                popularised in the 1960s with the release of Letraset sheets
              </div>
            </div>
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Phat_Thai_kung_Chang_Khien_street_stall.jpg/1280px-Phat_Thai_kung_Chang_Khien_street_stall.jpg"
              width="250px"
              alt="ผัดไทย"
            />
          </div>
          {this.state.foods.map((food) => {
            if (food.name === "ผัดไทย") {
              return (
                <Food
                  key={food.name}
                  count={food.count}
                  onVote={() => this.onVote(food.name)}
                  onUnVote={() => this.onUnVote(food.name)}
                />
              );
            } else {
              return null;
            }
          })}
        </div>
      </div>
    );
  }
}

export default App;
