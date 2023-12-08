// YourPage.tsx
'use client'
import React from 'react';
import Container from '../../styles/Container';
import {Image} from 'react-bootstrap';
import FormFileExample from './Form';
import FillExample from '../navbar';

function YourPage() {
    return (
        <Container className="d-flex align-items-center justify-content-center">
            <Image 
            src="./StatusBar.png"  
            alt="" 
            width={390}
            height={47}
            />
            <Image 
            className='mx-auto d-block'
            src="./Logo.png"  
            alt="" 
            width={170}
            height={125.54}
            style={{ marginTop: '100'}}
            />
            {/* <FormFileExample />
            <FillExample /> */}
            <div 
            className='mb-4' 
            style={{ 
                position: 'fixed', 
                bottom: '0', 
                left: '50%', 
                transform: 'translateX(-50%)', 
                color: '#767676' 
                }}>
                <p>Version 1.0</p>
            </div>
            <Image 
            className='home-indicator'
            src="./HomeIndicator.png"  
            alt="" 
            width={392}
            height={34}
            style={{ position: 'fixed', bottom: '0'}}
            />
        </Container>
    );
}

export default YourPage;
