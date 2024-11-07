'use client'
import { useTelegram } from "@/components/telegram/provider";
import React, { useMemo } from "react";

// const Page = () => {
// 	const { webApp } = useTelegram();
// 	const initData = useMemo(() => webApp && webApp.initData, [webApp]);
// 	getUser(initData);
// }

// const getUser = (initData: string) => {
//   return fetcher(null, `${getHost()}/user/info`, {
//     method: "GET",
//     headers: new Headers({
//       "Content-Type": "application/json",
//       Authorization: `tma ${initData}`,
//     }),
//   });
// };

export default function New() {
  return (
    <div>
      <p>testcode</p> 
    </div>
  )
}