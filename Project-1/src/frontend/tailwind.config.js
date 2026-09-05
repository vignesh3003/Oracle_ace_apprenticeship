/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        oracle: {
          red: '#C74634',
          dark: '#161513',
          gray: '#2C2A29',
          light: '#F8F9FA',
          accent: '#31006F',
        },
      },
    },
  },
  plugins: [],
};
