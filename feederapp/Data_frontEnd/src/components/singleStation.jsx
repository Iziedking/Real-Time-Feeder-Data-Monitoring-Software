import React from 'react';

const CardItem = ({ bgColor = "white", text, shadow = true }) => {
  return (
    <div className={`w-[115px] h-[45px] relative rounded-lg ${shadow ? "shadow" : ""}`}>
      <div
        className={`w-[115px] h-[45px] left-0 top-0 absolute rounded-lg`}
        style={{ backgroundColor: bgColor }}
      />
      <div
        className="absolute w-full h-full flex items-center justify-center text-center text-black text-[11px] font-normal font-['Montserrat'] leading-none px-2"
      >
        {text}
      </div>
    </div>
  );
};

export default CardItem;
