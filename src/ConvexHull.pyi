class ConvexHull(_QhullUser):
    simplices: NDArray[np.intc]
    neighbors: NDArray[np.intc]
    equations: NDArray[np.float64]
    coplanar: NDArray[np.intc]
    good: None | NDArray[np.bool_]
    volume: float
    area: float
    nsimplex: int

    def __init__(
        self,
        points: ArrayLike,
        incremental: bool = ...,
        qhull_options: None | str = ...
    ) -> None: ...
    def _update(self, qhull: _Qhull) -> None: ...
    def add_points(self, points: ArrayLike,
                   restart: bool = ...) -> None: ...
    @property
    def points(self) -> NDArray[np.float64]: ...
    @property
    def vertices(self) -> NDArray[np.intc]: ...