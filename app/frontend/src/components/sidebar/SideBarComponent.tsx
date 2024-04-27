import React, { useState, ReactNode } from 'react';
import './SideBarComponent.css';

interface SidebarComponenetProp {
    title?: String;
    Icon: React.FunctionComponent<{ className?: string }>;
    content: ReactNode;
    onSave?: () => void;
}


const Dropdown : React.FC<SidebarComponenetProp> = ({title, Icon, content, onSave}) => {
    const [isOpen, setIsOpen] = useState(false);

    const handleSave = () => {
        if (onSave) {
            onSave();
        }
        setIsOpen(false);
    };

    return (
        <div className="sidebarcomponent-container">
            <button className="sidebarcomponent-button" onClick={() => setIsOpen(!isOpen)}>
                <Icon className="sidebarcomponent-icon" />
            </button>
            <div className="sidebarcomponent-popup-container" style={{ display: isOpen ? 'block' : 'none' }}>
                <div className="sidebarcomponent-popup">
                    {title && <h2 className="sidebarcomponent-title">{title}</h2>}
                    {content}
                <div className="buttons">
                    {onSave &&
                        <button onClick={handleSave}>Save</button>
                    }
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dropdown;
