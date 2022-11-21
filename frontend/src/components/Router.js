import { Routes, Route } from "react-router-dom";
import Regions from "./pages/Regions";
import Locations from "./pages/Locations";

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<Regions />} />
      <Route path="/location/:region_id" element={<Locations />} />
    </Routes>
  );
}
