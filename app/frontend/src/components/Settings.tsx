import React, { useState } from 'react';
import './Settings.css';

interface SettingsProps {
  onClose: () => void;

  onUpdateSettings: (newSettings: {
      useSVD: boolean;
      maxResults: number
  }) => void;

  settings: {
      useSVD: boolean;
      maxResults: number
  };
}

const Settings: React.FC<SettingsProps> = ({ onClose, onUpdateSettings, settings }) => {
  const [useSVD, setSetting1] = useState(settings.useSVD);
  const [maxResults, setSetting2] = useState(settings.maxResults);

  const handleClose = () => {
    onClose();
  };

  const handleSave = () => {
    const newSettings = { useSVD, maxResults };
    onUpdateSettings(newSettings);
    handleClose();
  };

  return (
    <div className="settings-popup">
      <h2>Settings</h2>
        <div className="setting">
            <label>Use SVD</label>
            <input type="checkbox" checked={useSVD} onChange={() => setSetting1(!useSVD)}/>
        </div>
        <div className="setting">
            <label>Max results</label>
            <input type="number" min="1" value={maxResults} onChange={(e) => setSetting2(parseInt(e.target.value))}/>
        </div>
        <div className="buttons">
        <button onClick={handleSave}>Save</button>
        <button onClick={handleClose}>Cancel</button>
      </div>
    </div>
  );
};

export default Settings;
