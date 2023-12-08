// YourPage.tsx
'use client'
import React from 'react';
import Container from '../../styles/Container';
import {Image} from 'react-bootstrap';
import FormFileExample from './Form';
import FillExample from '../navbar';

function YourPage() {
    return (
        <Container className="bg-light">
            <Image 
            src="./StatusBar.png"  
            alt="" 
            width={390}
            height={47}
            />
            <Image 
            src="./Logo.png"  
            alt="" 
            width={392}
            height={34}
            />
            <FormFileExample />
            <FillExample />
            <Image 
            src="./HomeIndicator.png"  
            alt="" 
            width={392}
            height={34}
            />
        </Container>
    );
}

export default YourPage;
