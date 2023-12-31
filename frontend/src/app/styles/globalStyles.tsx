// GlobalStyles.ts

import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  :root {
    --foreground-rgb: 0, 0, 0;
    --background-start-rgb: 0, 0, 0;
    --background-end-rgb: 0, 0, 0;
  }

  body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif; /* Choose your preferred font */
    background-color: #FF0000 !important;
    /* Add any other global styles here */
  }
`;

export default GlobalStyles;
