import React from 'react';
import HeaderText from './components/HeaderText';
import Footer from './components/Footer';

import './styles/App.css';
import NavButton from './components/NavButton';

function App() {
  const subText = (
    <p id="underText">Inspired by <a href="https://heardle.app">Heardle</a>. Now with daily, practice, and challenge modes (including genre selection).</p>
  )

  return (
    <div className="App">
      <HeaderText text="Songle" doAnimation={true} subText={subText} isGame={false} />
      <div id="buttonHolder">
        <NavButton route="/daily" innerText="Daily" />
        <NavButton route="/practice" innerText="Practice" />
        <NavButton route="/challenge" innerText="Challenge" />
        <NavButton route="/about" innerText="About" />
      </div>
      <div id="key">
        <p><strong>📅 Daily:</strong> A new song daily; changes midnight EST.<br />
        <strong>✍️ Practice:</strong> Practice your song-recognition powers. Choose the genre if you'd like.<br />
        <strong>🔥 Challenge:</strong> Choose a song and challenge your friends to recognize the song.<br />
        <strong>⁉️ About:</strong> Learn more about Songle.</p>  
      </div>
      <Footer />
    </div>
  )
}

export default App;
