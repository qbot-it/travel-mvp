// YourPage.tsx
'use client'
import React from 'react';
import Container from '../../styles/Container';
import {Image} from 'react-bootstrap';
import FormFileExample from './Form';
import FillExample from '../navbar';

function YourPage() {
    return (
        <Container>
            <Image 
            src="./StatusBar.png"  
            alt="" 
            width={390}
            height={47}
            />
            <FormFileExample />
            <FillExample />
        </Container>
    );
}

export default YourPage;
