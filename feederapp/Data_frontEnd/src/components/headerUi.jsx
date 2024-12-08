import React from 'react';

const HeaderUI = () => {
  return (
    <div>
      <div className="w-[1590px] h-14 px-4 py-2 bg-white justify-between items-center inline-flex">
        <div className="w-6 h-6 p-1 justify-center items-center flex" />
        <div className="justify-end items-center gap-6 flex">
          <div className="text-[#026487] text-[28px] font-normal font-['Montserrat'] leading-9">
            BEDC LIVE FEEDER FEED
          </div>
        </div>
       {/*  <div className="w-6 h-6 px-1.5 justify-center items-center flex" />
        <div className="justify-end items-center gap-6 flex">
          <div className="text-[#026487] text-[22px] font-bold font-['Montserrat'] leading-9">
            AYEDE TRANSMISSION STATION
          </div>
        </div> */}
        <div className="justify-end items-center gap-5 flex">
          <div className="text-[#026487] text-base font-bold font-['Montserrat'] leading-normal tracking-wide">
            Home
          </div>
        </div>
      </div>
      <div className="w-14 h-14 p-2 bg-[#026487] rounded-lg flex-col justify-between items-start inline-flex">
        <div className="p-2 justify-start items-center gap-2.5 inline-flex">
          <div className="grow shrink basis-0 self-stretch px-[3px] py-1.5 justify-center items-center flex" />
        </div>
      </div>
       {/* Multi-Station View Section */}
       <div className="w-full flex justify-center items-center mt-6">
        <div className="w-[421px] h-8 relative flex items-center justify-center">
          <div className="w-full h-full absolute bg-[#026487] rounded-lg"></div>
          <div className="text-white text-base font-bold font-['Montserrat'] leading-normal tracking-wide z-10">
            MULTI-STATION VIEW
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeaderUI;
