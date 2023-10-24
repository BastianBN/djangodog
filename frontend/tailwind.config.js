/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx,svg,jpg,png}"],
  theme: {
    extend: {
      backgroundSize: {
        "size-200": "200% 200%",
      },
      backgroundPosition: {
        "pos-0tr": "100% 0%",
        "pos-100tr": "0% 100%",
        "pos-0br": "0% 0%",
        "pos-100br": "100% 100%",
      },
      colors: {
        transparent: "transparent",
        black: "black",
        linkedin: "#0077b5",
        github: "#333",
        mail: "#db0e0e",
        current: "currentColor",
        melatonin: {
          100: "#ffcbf2",
          200: "#f3c4fb",
          300: "#ecbcfd",
          400: "#e5b3fe",
          500: "#e2afff",
          600: "#deaaff",
          700: "#d8bbff",
          800: "#d0d1ff",
          900: "#c8e7ff",
        },
      },
      screens: {
        sm: "640px",
        // => @media (min-width: 640px) { ... }

        md: "768px",
        // => @media (min-width: 768px) { ... }

        lg: "1024px",
        // => @media (min-width: 1024px) { ... }

        xl: "1280px",
        // => @media (min-width: 1280px) { ... }

        "2xl": "1536px",
        // => @media (min-width: 1536px) { ... }
      },
    },
  },
  plugins: [],
};