import React, { useState, useEffect } from 'react';
import './App.css';
// @ts-ignore
import { ReactComponent as SearchIcon } from "./assets/search-icon.svg"
import SearchResult, { SearchResultProp } from './components/SearchResult';
import Settings from "./components/Settings";

const App: React.FC = () => {
    const [isSearching, setIsSearching] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState<SearchResultProp[]>([]);
    const [showSettings, setShowSettings] = useState(false);
    const [settings, setSettings] = useState({ useSVD: false, maxResults: 10 });

    const handleSearch = () => {
        setIsSearching(true);
        setSearchResults([]);

        fetch(`${process.env.REACT_APP_API_URL}/query?q=${searchTerm}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data: SearchResultProp[]) => {
                setSearchResults(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    };

    const handleLogoClick = () => {
        setIsSearching(false);
        setSearchResults([]);
    };

    useEffect(() => {
        const handleScroll = (event : WheelEvent) => {
            const searchResultsDiv = document.querySelector('.search-results');
            if (searchResultsDiv) {
                searchResultsDiv.scrollTop += event.deltaY;
            }
        };

        window.addEventListener('wheel', handleScroll);

        return () => {
            window.removeEventListener('wheel', handleScroll);
        };
    }, []);

    const toggleSettings = () => {
        setShowSettings(!showSettings);
    };

    const updateSettings = (newSettings: any) => {
        setSettings(newSettings);
    };

  return (
    <div className="App">
      <div className="container">
        <h1 className={`logo ${isSearching ? 'searching' : ''}`} onClick={handleLogoClick}>Searchify</h1>
        <button className="settings-button" onClick={toggleSettings}>Settings</button>
        {showSettings && <Settings onClose={toggleSettings} onUpdateSettings={updateSettings} settings={settings}/>}
        <div className="search-box">
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search..."
            className="search-input"
          />
          <button onClick={handleSearch} className="search-button">
            <SearchIcon className="search-icon"/>
          </button>
        </div>
        <div className="search-results" style={{height: isSearching ? '100%' : '0%'}}>
          {searchResults.map((result, index) => (
            <SearchResult
              key={index}
              name={result.name}
              url={result.url}
              description={result.description}
              similarity={result.similarity}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
