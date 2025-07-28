/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.py',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      // Custom colors theo design hiện tại
      colors: {
        'sunny': {
          pink: {
            50: '#fef2f5',
            100: '#fde6ea', 
            200: '#fbd0db',
            300: '#f7aabf',
            400: '#f27ba0',
            500: '#FF6B9D', // Màu chính
            600: '#e8407a',
            700: '#d12862',
            800: '#b11d52',
            900: '#9a1c4a',
          },
          teal: {
            50: '#f0fdfa',
            100: '#ccfbf1',
            200: '#99f6e4',
            300: '#5eedd5',
            400: '#4ECDC4', // Màu chính
            500: '#14b8a6',
            600: '#0d9488',
            700: '#0f766e',
            800: '#115e59',
            900: '#134e4a',
          },
          yellow: {
            50: '#fefce8',
            100: '#fef9c3',
            200: '#fef08a',
            300: '#fde047',
            400: '#FFE066', // Màu chính
            500: '#eab308',
            600: '#ca8a04',
            700: '#a16207',
            800: '#854d0e',
            900: '#713f12',
          }
        },
        // Màu cho trạng thái
        success: '#10B981',
        warning: '#F59E0B', 
        error: '#EF4444',
        info: '#3B82F6'
      },
      
      // Typography
      fontFamily: {
        'display': ['Nunito', 'Inter', 'system-ui', 'sans-serif'],
        'body': ['Inter', 'Nunito', 'system-ui', 'sans-serif'],
      },
      
      // Animations tùy chỉnh
      animation: {
        'float': 'float 3s ease-in-out infinite',
        'bounce-slow': 'bounce 2s infinite',
        'slide-in-up': 'slideInUp 1s ease-out',
        'fade-in': 'fadeIn 0.8s ease-out',
        'scale-in': 'scaleIn 0.6s ease-out',
        'gradient': 'gradient 8s ease infinite',
      },
      
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
        slideInUp: {
          '0%': {
            opacity: '0',
            transform: 'translateY(30px)'
          },
          '100%': {
            opacity: '1', 
            transform: 'translateY(0)'
          }
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        scaleIn: {
          '0%': {
            opacity: '0',
            transform: 'scale(0.9)'
          },
          '100%': {
            opacity: '1',
            transform: 'scale(1)'
          }
        },
        gradient: {
          '0%, 100%': {
            'background-size': '200% 200%',
            'background-position': 'left center'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right center'
          },
        },
      },
      
      // Gradient backgrounds
      backgroundImage: {
        'sunny-gradient': 'linear-gradient(135deg, #FFE066 0%, #FF6B9D 50%, #4ECDC4 100%)',
        'pink-teal': 'linear-gradient(135deg, #FF6B9D, #4ECDC4)',
        'teal-green': 'linear-gradient(135deg, #4ECDC4, #44A08D)',
        'hero-pattern': 'linear-gradient(135deg, #FFE066 0%, #FF6B9D 50%, #4ECDC4 100%)',
      },
      
      // Box shadows
      boxShadow: {
        'sunny': '0 10px 25px rgba(255, 107, 157, 0.3)',
        'sunny-lg': '0 20px 40px rgba(255, 107, 157, 0.4)',
        'teal': '0 10px 25px rgba(78, 205, 196, 0.3)',
        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
        card: '0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06)',
        'card-hover': '0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05)',
      },
      
      // Backdrop blur
      backdropBlur: {
        'xs': '2px',
      },
      
      // Spacing
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      
      // Border radius
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
        '3xl': '2rem',
      },
      
      // Z-index
      zIndex: {
        '60': '60',
        '70': '70',
        '80': '80',
        '90': '90',
        '100': '100',
      }
    },
  },
  plugins: [
    // Plugin để thêm utilities tùy chỉnh
    function({ addUtilities, theme }) {
      const newUtilities = {
        '.glass': {
          background: 'rgba(255, 255, 255, 0.1)',
          'backdrop-filter': 'blur(10px)',
          'border': '1px solid rgba(255, 255, 255, 0.2)',
        },
        '.glass-dark': {
          background: 'rgba(0, 0, 0, 0.1)',
          'backdrop-filter': 'blur(10px)',
          'border': '1px solid rgba(255, 255, 255, 0.1)',
        },
        '.text-shadow': {
          'text-shadow': '2px 2px 4px rgba(0,0,0,0.7)',
        },
        '.text-shadow-sm': {
          'text-shadow': '1px 1px 2px rgba(0,0,0,0.7)',
          
        },
      }
      addUtilities(newUtilities)
    },
    
    // Aspect ratio plugin (built-in từ Tailwind v3.0)
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}