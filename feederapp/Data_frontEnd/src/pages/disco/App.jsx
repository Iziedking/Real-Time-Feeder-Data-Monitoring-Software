import React from 'react';
import HeaderUI from '../../components/headerUi';
import CardItem from '../../components/singleStation';

function App() {
  return (
    <div>
      <HeaderUI />
      <div className="flex flex-col items-center p-8">
        {/* Top-level card */}
        <div className="relative">
          <CardItem bgColor="white" text="EXPRESS" />
          {/* Line going down */}
          <div className="absolute top-[45px] left-1/2 transform -translate-x-1/2 w-[2px] h-[50px] bg-black"></div>
        </div>

        {/* Second row of cards */}
        <div className="flex gap-16 mt-12 relative">
          {/* Left child */}
          <div className="relative">
            <CardItem bgColor="white" text="EXPRESS T1, 15MVA" />
            {/* Line connecting to top */}
            <div className="absolute top-[-50px] left-1/2 transform -translate-x-1/2 w-[2px] h-[50px] bg-black"></div>
          </div>

          {/* Middle child */}
          <div className="relative">
            <CardItem bgColor="white" text="EXPRESS T2, 15MVA" />
            {/* Line connecting to top */}
            <div className="absolute top-[-50px] left-1/2 transform -translate-x-1/2 w-[2px] h-[50px] bg-black"></div>
          </div>

          {/* Right child */}
          <div className="relative">
            <CardItem bgColor="#fff112" text="QUATUM PLASTIC INDUSTRIES 5MVA" />
            {/* Line connecting to top */}
            <div className="absolute top-[-50px] left-1/2 transform -translate-x-1/2 w-[2px] h-[50px] bg-black"></div>
          </div>
        </div>

        {/* Horizontal line connecting the second row */}
        <div className="absolute top-[140px] w-[300px] h-[2px] bg-black"></div>
      </div>
    </div>
  );
}

export default App;
