import React from "react";
import CircularProgress from "@mui/material/CircularProgress";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardActionArea from "@mui/material/CardActionArea";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import { useQuery } from "react-query";
import { useNavigate } from "react-router-dom";

export default function Regions() {
  const { isLoading, error, data } = useQuery("getRegions", () =>
    fetch("http://127.0.0.1:8000/regions/").then((res) => res.json())
  );
  const navigate = useNavigate();

  if (isLoading) {
    return <CircularProgress />;
  }
  if (error) {
    return (
      <Alert severity="error">
        <AlertTitle>Error</AlertTitle>
        An error occurred while calling the API
      </Alert>
    );
  }
  return (
    <>
      <Typography variant="h3" mb={4}>
        Regions
      </Typography>
      <Grid container rowSpacing={2} columnSpacing={2}>
        {data.regions.map(({ name: name, poke_id: region_id }) => (
          <Grid item key={region_id}>
            <Card sx={{ height: "100%", width: 400 }}>
              <CardActionArea onClick={() => navigate(`${name}/${region_id}`)}>
                <CardContent sx={{ marginLeft: "auto", marginRight: "auto" }}>
                  <Typography
                    variant="h4"
                    sx={{
                      height: 250,
                      textTransform: "capitalize",
                      textAlign: "center",
                    }}
                  >
                    {name}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
}
