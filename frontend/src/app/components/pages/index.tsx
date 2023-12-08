// YourPage.tsx
'use client'
import React from 'react';
import Container from '../../styles/Container';
import {Button, Image, Stack} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './startPage.css';

function YourPage() {
    return (
        <Container>
            <Image 
            src="./StatusBar.png"  
            alt="" 
            width={390}
            height={47}
            />
            <Stack gap={200}>
                <div>
                    <Image 
                    className='mx-auto d-block'
                    src="./Logo.png"  
                    alt="" 
                    width={170}
                    height={125.54}
                    style={{ marginTop: '100'}}
                    />
                </div>
                <div className='mx-auto d-block'>
                    <Button 
                    className='button-start'
                    variant="warning"
                    >
                    Get Started
                    </Button>
                </div>
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
            </Stack>
            
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
