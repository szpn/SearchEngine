import React, {useState} from 'react';
// @ts-ignore
import {ReactComponent as SettingsIcon} from "../assets/settings-icon.svg"
import './Settings.css';

interface SettingsProps {

    onUpdateSettings: (newSettings: {
        useSVD: boolean;
        maxResults: number
    }) => void;

    settings: {
        useSVD: boolean;
        maxResults: number
    };
}

const Settings: React.FC<SettingsProps> = ({onUpdateSettings, settings}) => {
    const [isOpen, setIsOpen] = useState(false);

    const [useSVD, setSetting1] = useState(settings.useSVD);
    const [maxResults, setSetting2] = useState(settings.maxResults);


    const handleSave = () => {
        const newSettings = {useSVD, maxResults};
        onUpdateSettings(newSettings);
        setIsOpen(false);
    };

    return (
        <div className="settings-container">
            <button className="settings-button" onClick={() => setIsOpen(!isOpen)}>
                <SettingsIcon class="settings-icon"/>
            </button>

            <div className="settings-popup-container" style={{display: isOpen ? 'block' : 'none'}}>
                <div className="settings-popup">
                    <h2>Settings</h2>

                    <div className="setting">
                        <label>Use SVD</label>
                        <input type="checkbox" checked={useSVD} onChange={() => setSetting1(!useSVD)}/>
                    </div>

                    <div className="setting">
                        <label>Max results</label>
                        <input type="number" min="1" value={maxResults}
                               onChange={(e) => setSetting2(parseInt(e.target.value))}/>
                    </div>

                    <div className="buttons">
                        {/*<button onClick={() => setIsOpen(false)}>Cancel</button>*/}
                        <button onClick={handleSave}>Save</button>
                    </div>
                </div>
            </div>
        </div>

    );
};

export default Settings;
